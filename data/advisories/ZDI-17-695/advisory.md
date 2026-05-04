# ZDI-17-695: SpiderControl SCADA Webserver iniNet Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-695
- **ZDI-CAN:** ZDI-CAN-4174
- **Date:** 2017-08-23
- **CVE:** CVE-2017-12694
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** SpiderControl
- **Affected Products:** SCADA Webserver iniNet
- **Credit:** juushya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-695/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of SpiderControl SCADA. Authentication is not required to exploit this vulnerability. The specific flaw exists within web server access to the scdefault directory. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose files accessible to the SYSTEM account.

## Additional Details

SpiderControl has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-17-234-03

## Disclosure Timeline

- 2017-02-10 - Vulnerability reported to vendor
- 2017-08-23 - Coordinated public release of advisory
