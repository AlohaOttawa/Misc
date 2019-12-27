import sqlite3

# Program to mimic SK tax tools


def UMR(tot_muni_prop_tax_rev, tot_val):
    # base level mill rate calculation using Saskatchewan rules
    # function needs the total desired municipal tax revenue and the total value of all properties

    return ((tot_muni_prop_tax_rev / tot_val) * 1000)

def Tax_SRM(property_assmt_val, mill_rate):
    # base level calculation for an individual property tax
    # function needs the property assessment value and the mill rate

    try:
        loc_taxSRM = ((property_assmt_val * mill_rate ) / 1000)
        return(loc_taxSRM)
    except ValueError as err:
        return(0)


def std_prop_tax(std_ind_prop_tax, std_mill_rate):
    # displays the mill rate and standard property tax
    # not needed for API

    print("The mill rate is: " + str(std_mill_rate))
    print("The standard individual property tax is: " + str(std_ind_prop_tax))

def mill_rate_factor_commercial(i_prop_tax, mrf):
    # mill rate factor calculation for commercial properties

    # comm_mrf = float(input("Enter the commercial mill rate factor: "))
    calc_comm_mrf = float(i_prop_tax * mrf)
    return calc_comm_mrf

def mill_rate_factor_residential(i_prop_tax, mrf):
    # mill rate factor calculation for residential properties

    # resi_mrf = float(input("Enter the residential mill rate factor: "))
    calc_resi_mrf = float(i_prop_tax * mrf)
    return calc_resi_mrf

def mill_rate_factor_agriculture(i_prop_tax, mrf):
    # mill rate factor calculation for agriculture

    # agri_mrf = float(input("Enter the agricultural mill rate factor: "))
    calc_agri_mrf = (i_prop_tax * mrf)
    return calc_agri_mrf

def mill_rate_factor(i_prop_tax, mrf):
    # mill rate factor main function
    # calls commercial, residential and agricultural functions for mill rate factor
    # NOTE THAT AGRICULTURE IS NOT CALLED YET
    # Remove the prints when converting to API

    commercial_property_tax = mill_rate_factor_commercial(i_prop_tax, mrf[0])
    residential_property_tax = mill_rate_factor_residential(i_prop_tax, mrf[1])

    print("The commercial tax is: " + str(commercial_property_tax))
    print("The residential tax is: " + str(residential_property_tax))

def min_property_tax(min_tax, ad_valorem_value):
    # using ad valorem tax approach, compare the value against the
    # minimum tax.  Use ad valorem if higher than minimum

    if ad_valorem_value > min_tax:
        return ad_valorem_value
    else:
        return min_tax

def base_tax(base_taxes):
    l_res_base_taxes = base_taxes[0]
    l_comm_base_tax = base_taxes[1]
    l_mill_rate = base_taxes[2]
    l_prop_value = base_taxes[3]
    base_tax_comm_tax = (l_res_base_taxes + ((l_prop_value * l_mill_rate) / 1000))
    base_tax_res_tax = (l_comm_base_tax + ((l_prop_value * l_mill_rate / 1000)))
    base_taxes[0] = base_tax_comm_tax
    base_taxes[1] = base_tax_res_tax
    return base_taxes


def stub():
    # stub for obtaining values from the user.  When moved to API / microservices, will be provided
    # by calling process


    stub_mun_tax_revenue = 478800
    stub_muni_assmt_value = 34200000
    stub_ind_prop_value = 81700
    u_mrf = [1.1, .8]

    # 0 -> commercial base tax
    # 1 -> residential base tax
    # 2 -> mill rate to use
    # 3 -> individual property assessment value to use
    u_base_taxes = [500, 400, 7, 81700]

    user_select = int(input("Please select:  1 - standard rate, 2 - mill rate factor, 3 - Minimum tax, 4 - Base tax: "))

    # if user selects 3, then get additional input before calling main()
    u_min_value = 0
    if user_select == 3:
        try:
            u_min_value = 200
            # u_min_value = float(input("Enter the minimum value: "))
            u_test = u_min_value + 1
        except ValueError:
            u_min_value = 0

    # if user_select == 4:
        # u_comm_base_tax = float(input("Enter the commercial base tax: "))
        # u_res_base_tax = float(input("Enter the residential base tax: "))
        # u_mill_rate = float(input("Enter the mill rate to use: "))
        # u_prop_value = float(input("Enter the individual property value: "))
        # u_base_taxes = [u_res_base_tax, u_comm_base_tax, u_mill_rate, u_prop_value]
        # calc_base_taxes = base_tax(u_base_taxes)

    # call main program
    # main(i_total_municipal_tax_revenue, i_total_municipal_value, i_property_assessment_value, user_select, min_tax)
    main(stub_mun_tax_revenue, stub_muni_assmt_value, stub_ind_prop_value, user_select, u_mrf, u_min_value, u_base_taxes)


def main(m_total_muni_tax_rev, m_total_muni_assessment, m_prop_assmt_val, m_calc_method, m_mrf, m_min_tax, m_base_taxes):

    # calculate the mill rate to be used in the SRM tax calculation
    mill_rate = UMR(m_total_muni_tax_rev, m_total_muni_assessment)

    # SRM tax calculation.
    TaxSRM = Tax_SRM(m_prop_assmt_val, mill_rate)

    # call the different tax functions
    if m_calc_method == 1:
        std_prop_tax(TaxSRM, mill_rate)
    elif m_calc_method == 2:
        mill_rate_factor(TaxSRM, m_mrf)
    elif m_calc_method == 3:
        calc_min_value = min_property_tax(m_min_tax,TaxSRM)
        print("Minimum value is: " + str(calc_min_value))
    elif m_calc_method == 4:
        calc_base_taxes = base_tax(m_base_taxes)
        print("The residential property tax is: " + str(calc_base_taxes[0]))
        print("The commercial property tax is: " + str(calc_base_taxes[1]))
    else:
        print("Call not valid")


stub()
