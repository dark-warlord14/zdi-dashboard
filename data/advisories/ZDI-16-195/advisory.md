# ZDI-16-195: Microsoft Internet Explorer Hidden Browser Window Restriction Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-195
- **ZDI-CAN:** ZDI-CAN-2916
- **Date:** 2016-03-10
- **CVE:** N/A
- **CVSS:** 6.4
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Simon Zuckerbraun - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-195/
## Vulnerability Details

This vulnerability allows remote attackers to create an invisible browser window on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the window.close() method. By issuing a particular sequence of script commands, an attacker can invoke window.close() and then continue executing script for an indefinite amount of time after the window has already been closed, and even after all browser windows have been closed. The user has no visual indication that script from the attacker's web page is still executing and there is no conventional UI available for stopping it.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-023

## Disclosure Timeline

- 2015-05-06 - Vulnerability reported to vendor
- 2016-03-10 - Coordinated public release of advisory
