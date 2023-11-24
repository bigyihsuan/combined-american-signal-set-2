def main():

    pass


signals = {

}


def generateSpriteSheets() -> str:
    # x = 17n, n >= 0
    # y = 33n, n >= 0

    return ""


VERSION = "0"
HEADER = f"""
grf {{
	grfid:                  "BY\\01\\01";
	name:                   string(STR_GRF_NAME);
	desc:                   string(STR_GRF_DESCRIPTION);
	url:                    string(STR_GRF_URL);
	version:                {VERSION};
	min_compatible_version: 0;
}}

if (!extended_feature_test("action3_signals_custom_signal_sprites")) {{
	error(FATAL, string(STR_UNSUPPORTED_VERSION));
}}
"""
FOOTER = """
switch(FEAT_SIGNALS, SELF, SABP_S, getbits(extra_callback_info2, 0, 8)){
    00: signal_SABP_S_STP;
    01: signal_SABP_S_CLR;
    05: signal_SABP_S_CLR;
    04: signal_SABP_S_CLR;
    03: signal_SABP_S_CLR;
    02: signal_SABP_S_APR;
}

switch(FEAT_SIGNALS, SELF, SABP_L, getbits(extra_callback_info2, 0, 8)){
    00: signal_SABP_L_STP;
    01: signal_SABP_L_CLR;
    05: signal_SABP_L_CLR;
    04: signal_SABP_L_CLR;
    03: signal_SABP_L_CLR;
    02: signal_SABP_L_APR;
}

switch(FEAT_SIGNALS, SELF, DAB_S, getbits(extra_callback_info2, 0, 8)){
    00: signal_DAB_S_STP;
    01: signal_DAB_S_CLR;
    05: signal_DAB_S_AAL;
    04: signal_DAB_S_APM;
    03: signal_DAB_S_AAP;
    02: signal_DAB_S_APR;
}

switch(FEAT_SIGNALS, SELF, DAP_S, getbits(extra_callback_info2, 0, 8)){
    00: signal_dAP_S_STP;
    01: signal_DAP_S_CLR;
    05: signal_DAP_S_CLR;
    04: signal_DAP_S_CLR;
    03: signal_DAP_S_MCL;
    02: signal_DAP_S_APR;
}

switch(FEAT_SIGNALS, SELF, DAB_L, getbits(extra_callback_info2, 0, 8)){
    00: signal_DAB_L_STP;
    01: signal_DAB_L_CLR;
    05: signal_DAB_L_AAL;
    04: signal_DAB_L_APM;
    03: signal_DAB_L_AAP;
    02: signal_DAB_L_APR;
}

switch(FEAT_SIGNALS, SELF, DAP_L, getbits(extra_callback_info2, 0, 8)){
    00: signal_DAP_L_STP;
    01: signal_DAP_L_CLR;
    05: signal_DAP_L_CLR;
    04: signal_DAP_L_CLR;
    03: signal_DAP_L_MCL;
    02: signal_DAP_L_APR;
}

switch(FEAT_SIGNALS, SELF, TAB_S, getbits(extra_callback_info2, 0, 8)){
    00: signal_TAB_S_STP;
    01: signal_TAB_S_CLR;
    05: signal_TAB_S_AAL;
    04: signal_TAB_S_APM;
    03: signal_TAB_S_APS;
    02: signal_TAB_S_APR;
}

switch(FEAT_SIGNALS, SELF, TAP_S, getbits(extra_callback_info2, 0, 8)){
    00: signal_TAP_S_STP;
    01: signal_TAP_S_CLR;
    05: signal_TAP_S_CLR;
    04: signal_TAP_S_LCL;
    03: signal_TAP_S_MCL;
    02: signal_TAP_S_SCL;
}

switch(FEAT_SIGNALS, SELF, TAB_L, getbits(extra_callback_info2, 0, 8)){
    00: signal_TAB_L_STP;
    01: signal_TAB_L_CLR;
    05: signal_TAB_L_AAL;
    04: signal_TAB_L_APM;
    03: signal_TAB_L_APS;
    02: signal_TAB_L_APR;
}

switch(FEAT_SIGNALS, SELF, TAP_L, getbits(extra_callback_info2, 0, 8)){
    00: signal_TAP_L_STP;
    01: signal_TAP_L_CLR;
    05: signal_TAP_L_CLR;
    04: signal_TAP_L_LCL;
    03: signal_TAP_L_MCL;
    02: signal_TAP_L_SCL;
}

switch(FEAT_SIGNALS, SELF, SABP, getbits(extra_callback_info2, 8, 8)){
    00: SABP_L;
    01: SABP_S;
}

switch(FEAT_SIGNALS, SELF, DAB, getbits(extra_callback_info2, 8, 8)){
    00: DAB_L;
    01: DAB_S;
}

switch(FEAT_SIGNALS, SELF, DAP, getbits(extra_callback_info2, 8, 8)){
    00: DAP_L;
    01: DAP_S;
}

switch(FEAT_SIGNALS, SELF, TAB, getbits(extra_callback_info2, 8, 8)){
    00: TAB_L;
    01: TAB_S;
}

switch(FEAT_SIGNALS, SELF, TAP, getbits(extra_callback_info2, 8, 8)){
    00: TAP_L;
    01: TAP_S;
}

switch(FEAT_SIGNALS, SELF, Singles, getbits(extra_callback_info2, 16, 8)){
    00: SABP;
    01: SABP;
    02: SABP;
    03: SABP;
    04: SABP;
    05: SABP;
    06: SABP;
    07: SABP;
}

switch(FEAT_SIGNALS, SELF, Doubles, getbits(extra_callback_info2, 16, 8)){
    00: DAB;
    01: DAP;
    02: DAP;
    03: DAP;
    04: DAP;
    05: DAP;
    06: DAP;
    07: DAP;
}

// switch(FEAT_SIGNALS, SELF, Triples, getbits(extra_callback_info2, 16, 8)){
//     00: TAB;
//     01: TAP;
//     02: TAP;
//     03: TAP;
//     04: TAP;
//     05: TAP;
//     06: TAP;
//     07: TAP;
// }

switch(FEAT_SIGNALS, SELF, listed_signals, signal_style){
    01: Singles;
    02: Doubles;
    // 03: Triples;
}

item (FEAT_SIGNALS, custom_signals, 0) {
    property{
        extra_aspects:      4;

        define_style:       1;
        style_name:         string(STR_SIG_SINGLE);
        style_electric_enabled: bitmask(SIGNAL_TYPE_NORMAL, SIGNAL_TYPE_PBS, SIGNAL_TYPE_PBS_ONEWAY);
        style_electric_enabled: bitmask(SIGNAL_TYPE_NORMAL, SIGNAL_TYPE_PBS, SIGNAL_TYPE_PBS_ONEWAY);

        define_style:       2;
        style_name:         string(STR_SIG_DOUBLE);
        style_electric_enabled: bitmask(SIGNAL_TYPE_NORMAL, SIGNAL_TYPE_PBS, SIGNAL_TYPE_PBS_ONEWAY);
        style_electric_enabled: bitmask(SIGNAL_TYPE_NORMAL, SIGNAL_TYPE_PBS, SIGNAL_TYPE_PBS_ONEWAY);

        // define_style:       3;
        // style_name:         string(STR_SIG_TRIPLE);
        // style_electric_enabled: bitmask(SIGNAL_TYPE_NORMAL, SIGNAL_TYPE_PBS, SIGNAL_TYPE_PBS_ONEWAY);
        // style_electric_enabled: bitmask(SIGNAL_TYPE_NORMAL, SIGNAL_TYPE_PBS, SIGNAL_TYPE_PBS_ONEWAY);
    }

    graphics {
        listed_signals
    }
}
"""
GRAPHICS = "gfx/1-and-2-head.png"

main()
