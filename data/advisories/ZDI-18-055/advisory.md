# ZDI-18-055: Advantech WebAccess picfile File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-055
- **ZDI-CAN:** ZDI-CAN-5057
- **Date:** 2018-01-05
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Zhou Yu
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-055/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Advantech WebAccess. Authentication is not required to exploit this vulnerability. The specific flaw exists within the picfile parameter in gmicons.asp. The issue results from the lack of proper validation of user-supplied data, which can allow for the upload of any file. An attacker can leverage this vulnerability to execute code in the context of the the web service.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-004-02

## Disclosure Timeline

- 2017-08-07 - Vulnerability reported to vendor
- 2018-01-05 - Coordinated public release of advisory
