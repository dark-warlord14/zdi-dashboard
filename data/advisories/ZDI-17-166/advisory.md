# ZDI-17-166: Hewlett Packard Enterprise Intelligent Management Center accessMgrServlet Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-166
- **ZDI-CAN:** ZDI-CAN-4122
- **Date:** 2017-03-11
- **CVE:** CVE-2017-5790
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** Jacob Baines - Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-166/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. Authentication is not required to exploit this vulnerability. The specific flaw exists within the accessMgrServlet servlet. The issue lies in the failure to properly validate user-supplied data which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute arbitrary code under the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://h20564.www2.hpe.com/hpsc/doc/public/display?docId=emr_na-hpesbhf03710en_us

## Disclosure Timeline

- 2016-11-03 - Vulnerability reported to vendor
- 2017-03-11 - Coordinated public release of advisory
