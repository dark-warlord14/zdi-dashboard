# ZDI-18-470: Advantech WebAccess NMS TFTP Unrestricted File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-470
- **ZDI-CAN:** ZDI-CAN-5476
- **Date:** 2018-05-18
- **CVE:** CVE-2018-7505
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-470/
## Vulnerability Details

This vulnerability allows remote attackers to execute code on vulnerable installations of Advantech WebAccess NMS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of the TFTP service. The issue results from the lack of proper validation of user-supplied data, which can allow for the upload of arbitrary files. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-135-01

## Disclosure Timeline

- 2017-12-08 - Vulnerability reported to vendor
- 2018-05-18 - Coordinated public release of advisory
- 2018-05-18 - Advisory Updated
