# ZDI-17-342: Hewlett Packard Enterprise Intelligent Management Center dbman Opcode 10007 Arbitrary File Deletion Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-342
- **ZDI-CAN:** ZDI-CAN-4386
- **Date:** 2017-05-15
- **CVE:** CVE-2017-5818
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:N/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** szitivi
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-342/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. Authentication is not required to exploit this vulnerability. The specific flaw exists within the dbman service, which listens on TCP port 2810 by default. The issue results from the lack of validation of file paths sent to an unlink call. This could all for the deletion of any file accessible by SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://h20564.www2.hpe.com/hpsc/doc/public/display?docId=emr_na-hpesbhf03745en_us

## Disclosure Timeline

- 2017-01-03 - Vulnerability reported to vendor
- 2017-05-15 - Coordinated public release of advisory
