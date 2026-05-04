# ZDI-14-099: Hewlett-Packard Universal CMDB Integration Service UploadScansServlet Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-099
- **ZDI-CAN:** ZDI-CAN-1977
- **Date:** 2014-04-17
- **CVE:** CVE-2013-6215
- **CVSS:** 8.5
- **CVSS Vector:** AV:N/AC:M/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Universal CMDB
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-099/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard Universal Configuration Management Database (CMDB). Authentication is required to exploit this vulnerability, but it is trivial to bypass. The specific flaw exists in the handling of requests to the Integration Service. The service exposes the UploadScanServlet which contains a flaw that allows attackers to create files at arbitrary locations with attacker controlled data. This vulnerability can be leveraged by an attacker to gain remote code execution under the context of SYSTEM.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c04219959

## Disclosure Timeline

- 2014-01-20 - Vulnerability reported to vendor
- 2014-04-17 - Coordinated public release of advisory
