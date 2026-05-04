# ZDI-14-383: Rockwell Automation Connected Components Workbench RA.ViewElements.Grid.1 Arbitrary Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-383
- **ZDI-CAN:** ZDI-CAN-2417
- **Date:** 2014-11-19
- **CVE:** CVE-2014-5424
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Rockwell Automation
- **Affected Products:** Connected Components Workbench
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-383/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Rockwell Automation Connected Components Workbench. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the RA.ViewElements.Grid.1 ActiveXControl method. By providing a malicious value to the LeftXOffset property, an attacker can write a four byte null value to an arbitrary location. An attacker could use this to execute arbitrary code in the context of the browser.

## Additional Details

Rockwell Automation has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-14-294-01

## Disclosure Timeline

- 2014-07-17 - Vulnerability reported to vendor
- 2014-11-19 - Coordinated public release of advisory
