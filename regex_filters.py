regex_filter = [
    "announc[a-z]{1,3} successful.{3,15}membership application",
    r"approv[a-z]{1,3} \$\d+(?:\.\d+)? (million|billion) spinoff of",
    r"(?<!(inability|unable) to )(obtain[a-z]{0,3}|receiv[a-z]{1,3}).{3,20}"
    "patent",
    r"acquir.{4,57}for \$\d+(?:\.\d+)? per share",
    "announc[a-z]{1,3} expansion of intellectual property",
    r"announc[a-z]{1,3} \$\d+(?:\.\d+)? (million|billion) "
    "(eloc|equity line of credit)",
    "announc.{1,12} internationalization .{2,20} patent portfolio",
    "transform[a-z]{0,5} (of )?luxury goods operation models",
    r"receiv[a-z]{1,3} (a )?\$\d+(?:\.\d+)? (million|billion) "
    "milestone payment",
    r"(announc[a-z]{1,3}|sign[a-z]{0,3}|enter[a-z]{0,3}) (into |a )?(crada|"
    r"cooperative research and development agreement( \(crada\))?) with",
    r"(near[a-z]{0,3}|approach[a-z]{0,3}) \$\d+(?:\.\d+)? (million|billion) "
    "deal",
    "select[a-z]{0,3} .{0,32} as exclusive supplier of",
    r"announc[a-z]{1,3} an \d+(?:\.\d+)?% year[ -]over[ -]year reduction "
    "of outstanding secured debt",
    r"volume grew ((?<![\S])0*+[4-9]\d|(?<![\S])0*+[1-9]\d{2,})(?:\.\d+)?%",
    "(announc[a-z]{1,3}|report[a-z]{0,3}) positive.{0,40} "
    "(top[ -]?line|durability) (data|results|outcomes)",
    r"(announc[a-z]{1,3}|authoriz[a-z]{1,3}) (\$\d+(?:\.\d+)? )?"
    "(million |billion )?(share|stock) (repurchase|buyback)",
    r"authorization to repurchase (up to )?\$\d+(?:\.\d+)? (million|billion)",
    "acquir[a-z]{1,3} (a )?portfolio of travel vaccines",
    r"sell.{0,50} for \$\d+(?:\.\d+)? million in cash",
    "(receiv[a-z]{1,3}|grant[a-z]{0,3}|issu[a-z]{1,3}) "
    "(a )?notice of allowance",
    "extend[a-z]{0,3} (stock|share) (buyback|repurchase) program",
    "announc[a-z]{1,3} price target of",
    "announc[a-z]{1,3} debt[ -]for[ -]equity exchange",
    "announc[a-z]{1,3} (the )?publication of (a )?"
    "(result[a-z]{0,3}|stud[a-z]{1,3}|review)",
    "open[a-z]{0,3} first retail",
    "(?<!(recently|previously|could not) )(receiv[a-z]{1,3}|announc[a-z]{1,3}"
    "|granted) fda approval",
    "receiv[a-z]{1,3} a grant approval",
    r"receiv[a-z]{1,3} \$\d+(?:\.\d+)? (million|billion) upfront payment",
    r"receiv[a-z]{1,3} an upfront payment of \$\d+(?:\.\d+)? (million|billion)"
    r"announc[a-z]{1,3} (up to |nearly)?\$\d+(?:\.\d+)? (million|billion)"
    " private placement financing",
    r"in deal for (up to |nearly )?\$\d+(?:\.\d+)? (million|billion)",
    "treatments? for early stage .{1,20} disease",
    r"announc[a-z]{1,3} plans? to raise \$\d+(?:\.\d+)? (million|billion)",
    "launch[a-z]{0,3} (a )?case study video highlighting the delivery of "
    "(a )?successful",
    r"(w[io]n[a-z]{0,1}|awarded) (a )?(multiple.{1}award )?\$\d+(?:\.\d+)? "
    r"(million|billion) (idiq |indefinite.{1}delivery.{1,2}"
    r"indefinite.{1}quantity \(idiq\) |indefinite.{1}delivery.{1,2}"
    "indefinite.{1}quantity )?contract",
    "announc[a-z]{1,3} definitive merger agreement",
    "celebrat[a-z]{1,3} discovery of",
    "complet[a-z]{1,3} (of )?business combination",
    "announc[a-z]{1,3} agreements for restructure of.{0,20} joint venture in",
    "(issu[a-z]{1,3}|grant[a-z]{0,3}) (an )?(emergency use authorization|eua)",
    r"disease control rate \(dcr\) (was|is) "
    r"((?<![\S])0*+[89]\d|(?<![\S])0*+[1-9]\d{2,})(?:\.\d+)?% (\(\d+/\d+\) )?"
    "for patients treated with",
    r"((?<![\S])0*+[89]\d|(?<![\S])0*+[1-9]\d{2,})(?:\.\d+)?% (dcr"
    r"|disease control rate( \(dcr\))?) after treatment",
    "sign[a-z]{0,3} an exclusive option agreement with .{2,50} to license "
    "technology",
    r"deal valued at(nearly |up to )? \$\d+(?:\.\d+)? (million|billion)",
    r"shareholders of .{2,50} (are set )?to receive \$\d+(?:\.\d+)? per share",
    r"to issue stock.{0,50} at a price of \$\d+(?:\.\d+)? per share",
    "receiv[a-z]{1,3} approval for and market[a-z]{0,3}",
    r"allow[a-z]{0,3} (us )?to proceed with (our|its) (phase \d )?"
    r"first[ -]in[ -]human (\(fih\) )?clinical trial",
    "announc[a-z]{1,3} (today )?that it has secured an equity stake in",
    "(?<!(recently|previously) )announc[a-z]{1,3} fda authorization",
    "(?<!(recently|previously) )announc[a-z]{1,3} agreement and plan of "
    "merger",
    "(enter[a-z]{0,3}|sign[a-z]{0,3}|execut[a-z]{1,3}|conclud[a-z]{1,3}|"
    "agree[a-z]{0,3}|finaliz[a-z]{1,3}|approv[a-z]{1,3}|endors[a-z]{1,3}|"
    "ratif[a-z]{1,4}|accept[a-z]{0,3}|confirm[a-z]{0,3}) (into )?(a )?"
    "(definitive )?securities purchase agreement",
    r"announc[a-z]{1,3} financing commitment for (up to )?\$\d+(?:\.\d+)? "
    "(million|billion)",
    "provided a.{1,16} immunogenicity update",
    r"((?<![\S])0*+[89]\d|(?<![\S])0*+[1-9]\d{2,})(?:\.\d+)?% (clinical "
    r"benefit rate (\(cbr\) )?|cbr )achieved",
    "achiev[a-z]{1,3} a "
    r"((?<![\S])0*+[89]\d|(?<![\S])0*+[1-9]\d{2,})(?:\.\d+)?%"
    r" (clinical benefit rate( \(cbr\))?|cbr)",
    "(securities purchase|subscription) agreement with.{0,50} institutional"
    " investor",
    r"the warrants will have an exercise price of \$\d+(?:\.\d+)? per share",
    r"announc[a-z]{1,3} the initiation of the final stage of the phase \d "
    "study",
    "announc[a-z]{1,3} (today )?that it has entered into a settlement "
    "agreement",
    r"\$\d+(?:\.\d+)? (million|billion) of new funding",
    r"\$\d+(?:\.\d+)? (million|billion) reduction of debt",
    "report[a-z]{0,3} (that )?data from a recent[a-z]{0,2} peer-reviewed "
    "(clinical )?study ",
    "announc[a-z]{1,3} (encouraging|positive) preliminary safety and efficacy "
    "data",
    "acquir[a-z]{1,3} entire intellectual property portfolio",
    "(purchas[a-z]{1,3}|acquir[a-z]{1,3}|buy[a-z]{0,3} out|tak[a-z]{1,3} over|"
    "merg[a-z]{1,3} with|acquir[a-z]{1,3} controlling interest"
    "|acquir[a-z]{1,3} ownership of).{0,30} through (a merger|an acquisition|"
    "a buyout|a takeover)",
    r"announc[a-z]{1,3} positive phase \d (cohort \d )?results",
    r"annouc[a-z]{1,3} positive final results of the phase \d",
    r"announc[a-z]{1,3} (up to )?\$\d+(?:\.\d+)? (million|billion) financing",
    "(finaliz[a-z]{1,3}|approv[a-z]{1,3}|sign[a-z]{0,3}|affirm[a-z]{0,3}|"
    "complet[a-z]{1,3}|conclud[a-z]{1,3})"
    "(a purchase agreement by sign[a-z]{3,5}|an agreement to purchase)",
    "(execut[a-z]{1,3}|sign[a-z]{0,3}|endors[a-z]{1,3}) a purchase "
    "(agreement|contract)",
    "announc[a-z]{1,3} strategic financing",
    "announc[a-z]{1,3} (today )?that it will (voluntarily )?transfer its stock"
    " exchange listing to the nasdaq stock market from the (new york stock"
    " exchange|nyse)",
    "(enter[a-z]{0,3}|announc[a-z]{1,3}) (into )?(an )?exclusive worldwide "
    "licens[a-z]{1,3} (and collaboration )?agreement",
    r"transaction valued at (approximately )?\$\d+(?:\.\d+)? "
    "(million|billion)",
    r"shareholders will receive \$\d+(?:\.\d+)? in cash",
    "shar[a-z]{1,3} detailed research data",
    "inhibition of tumor (metastasis|spread)",
    "demonstrat[a-z]{1,3} significantly greater tumor inhibition",
    r"currently working to move these.{0,40} discoveries towards phase \d "
    "clinical trials",
    "(successful|positive),? preclinical (results|data)",
    r"annouc[a-z]{1,3} (institutional review board( \(irb\))?|irb) approval "
    r"for fda[ -]cleared phase \d",
    "authoriz[a-z]{1,5} (by|from) (the )?fda",
    r"announc[a-z]{1,3} updated mri results from the phase \d",
    "acqui[a-z]{2,6} (of )?product rights? and patents?",
    r"to receive upfront payment of \$\d+(?:\.\d+)? (million|billion)",
    "announc[a-z]{1,3} it has contracted to sell",
    "announc[a-z]{1,3} department of defense dapa registration",
    r"the facility is anticipated to generate an estimated \$\d+(?:\.\d+)?"
    r"(\d+(?:\.\d+)?)? (million|billion) in annual revenue",
    r"for proceeds of (approximately )?\$\d+(?:\.\d+)? (million|billion)",
    "announc[a-z]{1,3} it has successfully completed the review of results "
    r"from milestone \$\d+(?:\.\d+)?",
    r"announc[a-z]{1,3} the successful completion of a phase \d clinical "
    "trial",
    r"leverag[a-z]{1,3} gpt-\d",
    r"(chatgpt|gpt-\d)[ -]powered functionality",
    r"first (chatgpt|gpt-\d)[ -]enabled",
]
