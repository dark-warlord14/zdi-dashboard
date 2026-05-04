# ZDI-17-330: Hewlett Packard Enterprise Network Automation TrueControl Management Engine Service FileServlet Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-330
- **ZDI-CAN:** ZDI-CAN-4217
- **Date:** 2017-05-11
- **CVE:** CVE-2017-5811
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Network Automation
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-330/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Hewlett Packard Enterprise Network Automation. Authentication is not required to exploit this vulnerability. The specific flaw exists within the FileServlet servlet. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose sensitive information under the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: http://h20564.www2.hpe.com/hpsc/doc/public/display?docId=emr_na-hpesbgn03740en_us

## Disclosure Timeline

- 2016-12-14 - Vulnerability reported to vendor
- 2017-05-11 - Coordinated public release of advisory
