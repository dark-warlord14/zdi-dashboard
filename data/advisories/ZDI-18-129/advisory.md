# ZDI-18-129: Dell EMC Storage Manager EmConfigMigration Servlet Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-129
- **ZDI-CAN:** ZDI-CAN-5293
- **Date:** 2018-01-18
- **CVE:** CVE-2017-14384
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Dell EMC
- **Affected Products:** Storage Manager
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-129/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Dell EMC Storage Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the EmConfigMigration servlet, which listens on TCP port 3033 by default. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to read any files accessible to the SYSTEM user.

## Additional Details

Dell EMC has issued an update to correct this vulnerability. More details can be found at: http://topics-cdn.dell.com/pdf/storage-sc2000_release%20notes24_en-us.pdf

## Disclosure Timeline

- 2017-10-12 - Vulnerability reported to vendor
- 2018-01-18 - Coordinated public release of advisory
