import re

def replace_out_res(text):
    # Define the regular expression pattern
    pattern = r'Out_Res(\d+)_(\d+)'
    
    # Define the replacement pattern
    replacement = lambda match: f'Out_Res[{match.group(1)}][{match.group(2)}]'
    
    # Replace all occurrences in the text
    replaced_text = re.sub(pattern, replacement, text)
    
    return replaced_text

# Example usage:
example_text = """
Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_0_0 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(In_OP0),      .In_OP1(In_OP1)      ,  .In_W(W0),  .In_Select(In_Select),    .Out_Res0(Out_Res0_0),    .Out_Res1(Out_Res0_1) ,     .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));
Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_0_1 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(In_OP2),      .In_OP1(In_OP3)      ,  .In_W(W0),  .In_Select(In_Select),    .Out_Res0(Out_Res0_2),    .Out_Res1(Out_Res0_3) ,     .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));
Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_0_2 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(In_OP4),      .In_OP1(In_OP5)      ,  .In_W(W0),  .In_Select(In_Select),    .Out_Res0(Out_Res0_4),    .Out_Res1(Out_Res0_5) ,     .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));
Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_0_3 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(In_OP6),      .In_OP1(In_OP7)      ,  .In_W(W0),  .In_Select(In_Select),    .Out_Res0(Out_Res0_6),    .Out_Res1(Out_Res0_7) ,     .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));
Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_0_4 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(In_OP8),      .In_OP1(In_OP9)      ,  .In_W(W0),  .In_Select(In_Select),    .Out_Res0(Out_Res0_8),    .Out_Res1(Out_Res0_9) ,     .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));
Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_0_5 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(In_OP10),     .In_OP1(In_OP11)     ,  .In_W(W0),  .In_Select(In_Select),    .Out_Res0(Out_Res0_10),   .Out_Res1(Out_Res0_11),     .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));
Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_0_6 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(In_OP12),     .In_OP1(In_OP13)     ,  .In_W(W0),  .In_Select(In_Select),    .Out_Res0(Out_Res0_12),   .Out_Res1(Out_Res0_13),     .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));
Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_0_7 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(In_OP14),     .In_OP1(In_OP15)     ,  .In_W(W0),  .In_Select(In_Select),    .Out_Res0(Out_Res0_14),   .Out_Res1(Out_Res0_15),     .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));
																																																				      
Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_1_0 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(Out_Res0_0),  .In_OP1(Out_Res0_2)  ,  .In_W(W1),  .In_Select(In_Select),    .Out_Res0(Out_Res1_0),    .Out_Res1(Out_Res1_1),      .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));
Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_1_1 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(Out_Res0_1),  .In_OP1(Out_Res0_3)  ,  .In_W(W2),  .In_Select(In_Select),    .Out_Res0(Out_Res1_2),    .Out_Res1(Out_Res1_3),      .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));
Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_1_2 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(Out_Res0_4),  .In_OP1(Out_Res0_6)  ,  .In_W(W1),  .In_Select(In_Select),    .Out_Res0(Out_Res1_4),    .Out_Res1(Out_Res1_5),      .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));
Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_1_3 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(Out_Res0_5),  .In_OP1(Out_Res0_7)  ,  .In_W(W2),  .In_Select(In_Select),    .Out_Res0(Out_Res1_6),    .Out_Res1(Out_Res1_7),      .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));
Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_1_4 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(Out_Res0_8),  .In_OP1(Out_Res0_10) ,  .In_W(W1),  .In_Select(In_Select),    .Out_Res0(Out_Res1_8),    .Out_Res1(Out_Res1_9),      .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));
Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_1_5 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(Out_Res0_9),  .In_OP1(Out_Res0_11) ,  .In_W(W2),  .In_Select(In_Select),    .Out_Res0(Out_Res1_10),   .Out_Res1(Out_Res1_11),     .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));
Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_1_6 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(Out_Res0_12), .In_OP1(Out_Res0_14) ,  .In_W(W1),  .In_Select(In_Select),    .Out_Res0(Out_Res1_12),   .Out_Res1(Out_Res1_13),     .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));
Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_1_7 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(Out_Res0_13), .In_OP1(Out_Res0_15) ,  .In_W(W2),  .In_Select(In_Select),    .Out_Res0(Out_Res1_14),   .Out_Res1(Out_Res1_15),     .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));
																																																				      
Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_2_0 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(Out_Res1_0),  .In_OP1(Out_Res1_4)  ,  .In_W(W3),  .In_Select(In_Select),    .Out_Res0(Out_Res2_0),    .Out_Res1(Out_Res2_1),      .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));
Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_2_1 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(Out_Res1_1),  .In_OP1(Out_Res1_5)  ,  .In_W(W4),  .In_Select(In_Select),    .Out_Res0(Out_Res2_2),    .Out_Res1(Out_Res2_3),      .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));
Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_2_2 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(Out_Res1_2),  .In_OP1(Out_Res1_6)  ,  .In_W(W5),  .In_Select(In_Select),    .Out_Res0(Out_Res2_4),    .Out_Res1(Out_Res2_5),      .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));
Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_2_3 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(Out_Res1_3),  .In_OP1(Out_Res1_7)  ,  .In_W(W6),  .In_Select(In_Select),    .Out_Res0(Out_Res2_6),    .Out_Res1(Out_Res2_7),      .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));
Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_2_4 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(Out_Res1_8),  .In_OP1(Out_Res1_12) ,  .In_W(W3),  .In_Select(In_Select),    .Out_Res0(Out_Res2_8),    .Out_Res1(Out_Res2_9),      .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));
Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_2_5 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(Out_Res1_9),  .In_OP1(Out_Res1_13) ,  .In_W(W4),  .In_Select(In_Select),    .Out_Res0(Out_Res2_10),   .Out_Res1(Out_Res2_11),     .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));
Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_2_6 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(Out_Res1_10), .In_OP1(Out_Res1_14) ,  .In_W(W5),  .In_Select(In_Select),    .Out_Res0(Out_Res2_12),   .Out_Res1(Out_Res2_13),     .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));
Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_2_7 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(Out_Res1_11), .In_OP1(Out_Res1_15) ,  .In_W(W6),  .In_Select(In_Select),    .Out_Res0(Out_Res2_14),   .Out_Res1(Out_Res2_15),     .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));																																																				      

Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_3_0 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(Out_Res2_0),  .In_OP1(Out_Res2_8)  , .In_W(W7),   .In_Select(In_Select),    .Out_Res0(Out_Res3_0),    .Out_Res1(Out_Res3_1),      .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));
Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_3_1 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(Out_Res2_1),  .In_OP1(Out_Res2_9)  , .In_W(W8),   .In_Select(In_Select),    .Out_Res0(Out_Res3_2),    .Out_Res1(Out_Res3_3),      .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));
Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_3_2 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(Out_Res2_2),  .In_OP1(Out_Res2_10) , .In_W(W9),   .In_Select(In_Select),    .Out_Res0(Out_Res3_4),    .Out_Res1(Out_Res3_5),      .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));
Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_3_3 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(Out_Res2_3),  .In_OP1(Out_Res2_11) , .In_W(W10),   .In_Select(In_Select),    .Out_Res0(Out_Res3_6),    .Out_Res1(Out_Res3_7),      .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));
Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_3_4 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(Out_Res2_4),  .In_OP1(Out_Res2_12) , .In_W(W11),   .In_Select(In_Select),    .Out_Res0(Out_Res3_8),    .Out_Res1(Out_Res3_9),      .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));
Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_3_5 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(Out_Res2_5),  .In_OP1(Out_Res2_13) , .In_W(W12),   .In_Select(In_Select),    .Out_Res0(Out_Res3_10),   .Out_Res1(Out_Res3_11),     .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));
Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_3_6 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(Out_Res2_6),  .In_OP1(Out_Res2_14) , .In_W(W13),   .In_Select(In_Select),    .Out_Res0(Out_Res3_12),   .Out_Res1(Out_Res3_13),     .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));
Top_PE #(.DATA_SIZE(DATA_SIZE)) PE_3_7 ( .Clk(Clk),.Rstn(Rst_n), .In_OP0(Out_Res2_7),  .In_OP1(Out_Res2_15) , .In_W(W14),   .In_Select(In_Select),    .Out_Res0(Out_Res3_14),   .Out_Res1(Out_Res3_15),     .In_Mod_Q(In_Mod_Q)   ,.In_Mod_Q_inv(In_Mod_Q_inv),  .In_R(In_R),   .In_R_RED_Squre(In_R_RED_Squre));
"""

# Call the function with the example text
replaced_text = replace_out_res(example_text)
print(replaced_text)