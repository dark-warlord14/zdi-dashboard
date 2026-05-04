# ZDI-11-309: Novell iPrint Client nipplib.dll GetDriverSettings Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-309
- **ZDI-CAN:** ZDI-CAN-1289
- **Date:** 2011-10-26
- **CVE:** CVE-2011-3173
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Novell
- **Affected Products:** iPrint
- **Credit:** gwslabs.com Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-309/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell iPrint Client. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within the nipplib.dll component. When handling the exposed method GetDriverSettings the application assembles a string for logging consisting of the hostname/port provided as a parameter. When building this message the process will blindly copy user supplied data into a fixed-length buffer on the stack. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the browser.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://download.novell.com/Download?buildid=bSpj4nhVEZ0~

## Disclosure Timeline

- 2011-07-21 - Vulnerability reported to vendor
- 2011-10-26 - Coordinated public release of advisory
