# ZDI-13-178: Cogent Datahub Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-178
- **ZDI-CAN:** ZDI-CAN-1915
- **Date:** 2013-07-26
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Cogent Real-Time Systems
- **Affected Products:** Cogent Datahub
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-178/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cogent Datahub. Authentication is not required to exploit this vulnerability. The specific flaw exists within the web server component's handling of HTTP headers. By sending an overlarge HTTP header, an attacker can overflow a fixed size stack buffer. This vulnerability allows for an attacker to execute arbitrary code in the context of the Datahub process.

## Additional Details

Cogent Real-Time Systems has issued an update to correct this vulnerability. More details can be found at: http://www.cogentdatahub.com/Info/130712_ZDI-CAN-1915_Response.html

## Disclosure Timeline

- 2013-06-25 - Vulnerability reported to vendor
- 2013-07-26 - Coordinated public release of advisory
