import streamlit as st
st.set_page_config(
    page_title="Energyviz",
    layout="wide"
)
def main():
    st.markdown("""
    <style>
    /* Sidebar styling - always blue with white text */
    [data-testid="stSidebar"] {
        background-color: #013e7d !important;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Headings color */
    h1, h2, h3, h4 {
        color: #007BFF !important;
    }
    
    /* ===== BASE DROPDOWN STYLES ===== */
    /* These will be overridden by the JavaScript theme detection */
    div[data-baseweb="select"] > div {
        border-radius: 25px !important;
        border: 2px solid #007BFF !important;
    }
    
    /* ===== JAVASCRIPT THEME DETECTION ===== */
    <script>
    function applyThemeStyles() {
        // Check if dark theme is active
        const isDark = document.body.classList.contains('st-emotion-cache-fg4pbf');
        
        // Select all dropdown containers
        const dropdowns = document.querySelectorAll('div[data-baseweb="select"] > div');
        
        dropdowns.forEach(dropdown => {
            if (isDark) {
                // Dark theme styles
                dropdown.style.backgroundColor = 'black';
                dropdown.style.color = 'white';
                
                // Find the selected value div and style it
                const selectedValue = dropdown.querySelector('div');
                if (selectedValue) {
                    selectedValue.style.color = 'white';
                }
            } else {
                // Light theme styles
                dropdown.style.backgroundColor = 'white';
                dropdown.style.color = 'black';
                
                // Find the selected value div and style it
                const selectedValue = dropdown.querySelector('div');
                if (selectedValue) {
                    selectedValue.style.color = 'black';
                }
            }
        });
        
        // Style dropdown menus
        const menus = document.querySelectorAll('div[data-baseweb="menu"]');
        menus.forEach(menu => {
            if (isDark) {
                menu.style.backgroundColor = 'black';
            } else {
                menu.style.backgroundColor = 'white';
            }
        });
        
        // Style menu items
        const menuItems = document.querySelectorAll('div[data-baseweb="menu"] > div > div');
        menuItems.forEach(item => {
            if (isDark) {
                item.style.backgroundColor = 'black';
                item.style.color = 'white';
            } else {
                item.style.backgroundColor = 'white';
                item.style.color = 'black';
            }
        });
    }
    
    // Run initially
    applyThemeStyles();
    
    // Run whenever the theme might change
    new MutationObserver(applyThemeStyles).observe(document.body, {
        attributes: true,
        attributeFilter: ['class']
    });
    </script>
    
    /* ===== COMMON STYLES ===== */
    
    </style>
    """, unsafe_allow_html=True)

    st.title("About")
    st.write(
        "Welcome to EnergyViz! A powerful and user-friendly tool designed to explore, "
        "analyze, and forecast energy consumption and capacity trends across Indian states and union territories. "
        "You can also gain information about different energy sources that will be mentioned here. "
        "So, let's dive into the world of EnergyViz."
    )

    st.header("Energy Source:")
    st.write(
        "Before performing analysis and prediction on energy resources, "
        "there should be a brief idea about the energy sources."
    )

    # Descriptions
    energy_info = {
        "Oil": "Oil is the most-used energy resource worldwide and provides more than 90% of global transportation energy. Because the majority of oil is produced by a limited number of countries, securing access to this resource has significant geopolitical consequences.Oil (also referred to as petroleum) is a depletable, non-renewable resource burned to convert chemical energy into heat, and a leading contributor to air pollution and climate change. It is a mixture of hydrocarbons found mostly in liquid form in porous rocks beneath the Earth’s surface. The process to extract and produce oil involves prospecting, drilling, completion, and production. Various refined products (e.g., gasoline, diesel, jet fuel) are obtained from processing crude oil, an energy-intensive process.Because of its high energy density, both by weight and volume, oil is very convenient for transport (where you have to carry your fuel with you). This makes it difficult to replace oil with less energy dense low-carbon alternatives.",
        "Coal": "Coal is a nonrenewable energy source that takes millions of years to create. It is a combustible black or brownish-black sedimentary rock composed mostly of carbon and hydrocarbons. The energy in coal comes from the remains of prehistoric plants and animals, making it part of the fossil fuels family. Coal formation began during the Carboniferous period (280 to 345 million years ago).  Much of the earth was covered with swamp during this time, and large amounts of plants and other organic matter grew. As the plants and other life forms died, they sank to the bottom of the swampy areas. They slowly decomposed, and formed peat—a soggy, dense, sponge-like material. Over time, the peat was buried and compressed under the earth’s surface. As the earth’s surface changed over millions of years, sand, clay and other minerals accumulated, burying the peat. Layer upon layer created heat and pressure, which compressed the peat into the hard substance we call coal.",
        "Wind": "Wind is used to produce electricity by converting the kinetic energy of air in motion into electricity. In modern wind turbines, wind rotates the rotor blades, which convert kinetic energy into rotational energy. This rotational energy is transferred by a shaft which to the generator, thereby producing electrical energy.Wind power has grown rapidly since 2000, driven by R&D, supportive policies and falling costs. Global installed wind generation capacity – both onshore and offshore – has increased by a factor of 98 in the past two decades, jumping from 7.5 GW in 1997 to some 733 GW by 2018 according to IRENA’s data. Onshore wind capacity grew from 178 GW in 2010 to 699 GW in 2020, while offshore wind has grown proportionately more, but from a lower base, from 3.1 GW in 2010 to 34.4 GW in 2020. Production of wind power increased by a factor of 5.2 between 2009 and 2019 to reach 1412 TWh.Both onshore and offshore wind still have tremendous potential for greater deployment and improvement, globally.",
        "Solar": (
            "Energy can be harnessed directly from the sun, even in cloudy weather. Solar energy is used worldwide and is increasingly popular for generating electricity, and heating or desalinating water. Solar power is generated in two main ways:\n\n"
            "Solar photovoltaic (PV) uses electronic devices, also called solar cells, to convert sunlight directly into electricity. It is one of the fastest-growing renewable energy technologies and is playing an increasingly important role in the global energy transformation. The total installed capacity of solar PV reached 710 GW globally at the end of 2020. About 125 GW of new solar PV capacity was added in 2020, the largest capacity addition of any renewable energy source.Solar PV is highly modular and ranges in size from small solar home kits and rooftop installations of 3-20 kW capacity, right up to systems with capacity in the hundreds of megawatts. It has democratised electricity production.The cost of manufacturing solar panels has plummeted dramatically in the past decade, making them not only affordable, but also often the cheapest form of electricity. Solar module prices fell by up to 93% between 2010 and 2020. During the same period, the global weighted-average levelised cost of electricity (LCOE) for utility-scale solar PV projects fell by 85%.\n\n"
            "Concentrated solar power (CSP) uses mirrors to concentrate solar rays. These rays heat fluid, which creates steam to drive a turbine and generate electricity. CSP is used to generate electricity in large-scale power plants. By the end of 2020, the global installed capacity of CSP was approaching 7 GW, a fivefold increase between 2010 and 2020. It is likely that some 150 MW was commissioned in 2020, although official statistics only captured 100 MW.It is possible to classify CSP systems according to the mechanism by which the solar collectors concentrate solar irradiation: either “linear concentrating” or “point concentrating” varieties. Most existing systems use linear concentrating systems called parabolic trough collectors. Solar towers, sometimes also known as power towers, are the most widely deployed point concentrating CSP technology, but represented only around a fifth of all systems deployed at the end of 2020.One of the main advantages of a CSP power plant over a solar PV power plant is that it can be equipped with molten salts in which heat can be stored, allowing electricity to be generated after the sun has set. As the market has matured, the cost of thermal energy storage has declined, making storage duration of 12 hours economic. This has resulted in an increase in the storage duration in CSP systems. CSP with low-cost thermal energy storage has the ability to integrate higher shares of variable solar and wind power, meaning that while often underappreciated, CSP could play an increasingly important role in the future."
        ),
        "Diesel":"Most freight and delivery trucks as well as trains, buses, boats, and farm, construction, and military vehicles, and some cars and light trucks have diesel engines. Diesel fuel is also used in diesel-engine generators to generate electricity, such as in remote villages in Alaska, among other locations around the world. Many industrial facilities, large buildings, institutional facilities, hospitals, and electric utilities have diesel generators for backup and emergency power supply.Diesel fuel is made from crude oil and biomassMost of the diesel fuel produced and consumed in the United States is refined from crude oil at petroleum refineries. U.S. petroleum refineries produce an average of 11 to 12 gallons of diesel fuel from each 42-gallon (U.S.) barrel of crude oil. The United States also produces and consumes biomass-based diesel fuels.Before 2006, most diesel fuel sold in the United States contained high quantities of sulfur. Sulfur in diesel fuel produces air pollution emissions that are harmful to human health. In 2006, the U.S. Environmental Protection Agency issued requirements to reduce the sulfur content of diesel fuel sold for use in the United States. The requirements were phased in over time, beginning with diesel fuel sold for vehicles used on roadways and eventually including all non-road diesel fuel. Diesel fuel now sold in the United States for on-highway use is ultra-low sulfur diesel (ULSD), which has a sulfur content of 15 parts per million or less. Most diesel fuel sold for off-highway (or non-road) use is also ULSD.",
        "Natural Gas":"Natural gas is a fossil fuel energy source. Natural gas contains many different compounds. The largest component of natural gas is methane, a compound with one carbon atom and four hydrogen atoms (CH4). Natural gas also contains smaller amounts of natural gas liquids (NGLs, which are also hydrocarbon gas liquids), and nonhydrocarbon gases, such as carbon dioxide and water vapor. We use natural gas as a fuel and to make materials and chemicals.Millions to hundreds of millions of years ago, the remains of plants and animals (such as diatoms) built up in thick layers on the earth’s surface and ocean floors, sometimes mixed with sand, silt, and calcium carbonate. Over time, these layers were buried under sand, silt, and rock. Pressure and heat changed some of this carbon and hydrogen-rich material into coal, some into oil (petroleum), and some into natural gas.",
        "Hydro":"Hydroenergy, or hydropower, is the energy derived from the movement of water. It is one of the oldest and most widely used forms of renewable energy. By capturing the kinetic energy of flowing or falling water, hydroelectric power plants generate electricity using turbines and generators.In a typical hydroelectric system, water is stored in a reservoir behind a dam. When released, the water flows through turbines, spinning them to generate electricity. The amount of energy produced depends on the volume of water and the height from which it falls (known as the head). In run-of-the-river systems, water flows naturally without large dams, but generates less power.Hydropower is a clean, renewable source of energy that doesn’t produce direct greenhouse gas emissions. It provides reliable, continuous electricity (called baseload power) and is also used to support peak demand through pumped storage systems. Additionally, hydropower plants can last for decades and support irrigation, flood control, and water supply.Despite its benefits, hydro energy can have environmental impacts, such as disrupting aquatic ecosystems, displacing communities, and altering natural water flow. Large dams may also lead to sediment buildup and affect downstream water availability.",
        "Bioenergy":"Bioenergy is a form of renewable energy that comes from biological sources, such as plants, animals, and organic waste. It is derived from biomass — materials like wood, crop residues, animal manure, and even food waste. Because these sources can be replenished naturally, bioenergy is considered sustainable when managed properly.Bioenergy can be produced through various processes, including burning biomass to generate heat or electricity, fermenting organic material to produce biogas, or converting crops into biofuels like ethanol and biodiesel. These energy forms can be used for cooking, heating, transportation, and electricity generation.Bioenergy helps reduce dependence on fossil fuels, lowers greenhouse gas emissions, and supports rural economies by creating jobs in agriculture and waste management. Additionally, it promotes waste recycling and offers a cleaner alternative to energy production.Despite its advantages, bioenergy also has challenges. If not managed sustainably, it can lead to deforestation, soil degradation, and food vs. fuel conflicts. It’s important to balance energy needs with environmental and social impacts to ensure long-term sustainability.",
        "Nuclear":"Nuclear energy is the energy released from the nucleus, or core, of atoms. It can be produced through two processes: fission (splitting atoms) and fusion (joining atoms). Currently, nuclear power plants primarily use fission to generate electricity by splitting the atoms of uranium or plutonium.In a nuclear reactor, uranium atoms are bombarded with neutrons, causing them to split and release a massive amount of heat energy. This heat turns water into steam, which then drives turbines connected to generators, producing electricity. The process is highly efficient and generates large amounts of energy from small amounts of fuel.Nuclear energy is considered a low-carbon energy source because it produces no greenhouse gas emissions during operation. It also provides a stable and reliable supply of electricity, making it a strong alternative to fossil fuels in the fight against climate change.Despite its benefits, nuclear energy has several challenges. Radioactive waste produced by nuclear reactors remains hazardous for thousands of years and must be stored safely. There are also concerns about nuclear accidents, such as those at Chernobyl and Fukushima, and the potential for nuclear technology to be used in weapons."
    }

    col1, col2 = st.columns(2)

    with col1:
        category = st.selectbox("Energy source category", ["Fossils", "Renewable"])

    with col2:
        if category == "Fossils":
            source = st.selectbox("Energy source", ["Oil", "Coal","Diesel","Natural Gas"])
        else:
            source = st.selectbox("Energy source", ["Wind", "Solar","Hydro","Bioenergy","Nuclear"])

    # Display based on selected source
    if source:
        st.header(source)
        st.write(energy_info[source])

if __name__ == "__main__":
    main()
