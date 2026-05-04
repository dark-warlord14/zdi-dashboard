# ZDI-14-139: Advantech WebAccess bwocxrun.ocx CreateProcess Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-139
- **ZDI-CAN:** ZDI-CAN-2095
- **Date:** 2014-05-19
- **CVE:** CVE-2014-0773
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Advantech
- **Affected Products:** Advantech WebAccess
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-139/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Advantech WebAccess. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the bwocxrun.ocx. The control exposes a scriptable method 'CreateProcess'. An attacker can exploit a flaw in the validation code within the method to execute arbitrary commands in the context of the browser.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-14-079-03

## Disclosure Timeline

- 2013-12-20 - Vulnerability reported to vendor
- 2014-05-19 - Coordinated public release of advisory
