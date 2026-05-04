# ZDI-06-025: Mozilla Firefox Javascript navigator Object Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-025
- **ZDI-CAN:** ZDI-CAN-055
- **Date:** 2006-07-26
- **CVE:** CVE-2006-3677
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Mozilla Firefox
- **Affected Products:** 1.5.x
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-025/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of the Mozilla Firefox web browser. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The flaw exists when assigning specific values to the window.navigator object. A lack of checking on assignment causes user supplied data to be later used in the creation of other objects leading to eventual code execution.

## Additional Details

Mozilla Firefox has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2006/mfsa2006-45.html

## Disclosure Timeline

- 2006-06-16 - Vulnerability reported to vendor
- 2006-07-26 - Coordinated public release of advisory
