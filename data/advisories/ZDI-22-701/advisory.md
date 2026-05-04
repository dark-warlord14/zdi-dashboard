# ZDI-22-701: (0Day) Delta Industrial Automation DRAS DSCP Scope File Parsing XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-701
- **ZDI-CAN:** ZDI-CAN-14654
- **Date:** 2022-04-28
- **CVE:** N/A
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N
- **Affected Vendors:** Delta Industrial Automation
- **Affected Products:** DRAS
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-701/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Delta Industrial Automation DRAS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of DSCP files. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose files in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 11/24/21 – ZDI reported the vulnerability to ICS-CERT 02/16/22 – ICS-CERT requested an extension until 03/31/22 02/18/22 – ZDI provided an extension until 03/31/22 04/06/22 – ZDI requested an update 04/07/22 – ZDI notified ICS-CERT of the intention to publish the case as 0-day advisory on 04/18/22 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-11-24 - Vulnerability reported to vendor
- 2022-04-28 - Coordinated public release of advisory
