# ZDI-14-137: Advantech WebAccess bwocxrun.ocx OpenUrlToBuffer Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-137
- **ZDI-CAN:** ZDI-CAN-2093
- **Date:** 2014-05-19
- **CVE:** CVE-2014-0771
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Advantech
- **Affected Products:** Advantech WebAccess
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-137/
## Vulnerability Details

This vulnerability allows remote attackers to access arbitrary files on vulnerable installations of Advantech WebAccess. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the bwocxrun.ocx cntrol. The control exposes a method 'OpenUrlToBuffer' which allows an attacker to access the contents of an arbitrary URL (including a file URL). An attacker can use this to access any file on the system or the content of any remote URL which is accessible in the current context of the browser.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-14-079-03

## Disclosure Timeline

- 2013-12-20 - Vulnerability reported to vendor
- 2014-05-19 - Coordinated public release of advisory
