# ZDI-17-837: Cisco License Manager Server ReportCSV Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-837
- **ZDI-CAN:** ZDI-CAN-4635
- **Date:** 2017-10-04
- **CVE:** CVE-2017-12263
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Cisco
- **Affected Products:** License Manager Server
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-837/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Cisco License Manager Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ReportCSV servlet, which listens on TCP port 8080 by default. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to read any files accessible to the SYSTEM user.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20171004-clm

## Disclosure Timeline

- 2017-03-30 - Vulnerability reported to vendor
- 2017-10-04 - Coordinated public release of advisory
