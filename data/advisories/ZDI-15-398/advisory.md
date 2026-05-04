# ZDI-15-398: Hewlett-Packard KeyView IDOL DOCX Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-398
- **ZDI-CAN:** ZDI-CAN-2885
- **Date:** 2015-08-24
- **CVE:** CVE-2015-5424
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** KeyView IDOL
- **Credit:** ASD - Vulnerability Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-398/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard KeyView IDOL. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within the handling of DOCX files. It is possible to trigger a use-after-free while handling tag data within a DOCX. A remote attacker could exploit this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20564.www2.hpe.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c04771027

## Disclosure Timeline

- 2015-05-19 - Vulnerability reported to vendor
- 2015-08-24 - Coordinated public release of advisory
