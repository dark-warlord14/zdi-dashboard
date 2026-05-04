# ZDI-19-228: (0Day) Microsoft Visual Studio settings XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-228
- **ZDI-CAN:** ZDI-CAN-7877
- **Date:** 2019-02-28
- **CVE:** N/A
- **CVSS:** 2.5
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Visual Studio
- **Credit:** Sooraj K S (@soorajks)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-228/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Visual Studio. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of SETTINGS files. Due to the improper restriction of XML External Entity (XXE) references, a specially crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of the current user.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with ZDI policies. 02/04/19 – ZDI sent the vulnerability report to the vendor and the vendor acknowledged the report 02/05/19 – The vendor replied with a tracking number 02/08/19 – The vendor advised ZDI that they were working on root cause analysis 02/12/19 – The vendor advised ZDI that they: “have decided that this case did not meet the bar for servicing as a Security Release. Engineering Team may or may not fix in the next version of the release.” 02/21/19 – ZDI notified the vendor that the report will be published as 0-day on 02/28/19 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2019-02-04 - Vulnerability reported to vendor
- 2019-02-28 - Coordinated public release of advisory
- 2019-05-30 - Advisory Updated
