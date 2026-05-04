# ZDI-15-405: Hewlett-Packard KeyView IDOL GIF Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-405
- **ZDI-CAN:** ZDI-CAN-2876
- **Date:** 2015-08-24
- **CVE:** CVE-2015-5417
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** KeyView IDOL
- **Credit:** ASD - Vulnerability Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-405/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard KeyView IDOL. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within the handling of GIF images. It is possible to trigger an out-of-bounds write by providing invalid LZW image data within a GIF. A remote attacker could exploit this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20564.www2.hpe.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c04771027

## Disclosure Timeline

- 2015-05-19 - Vulnerability reported to vendor
- 2015-08-24 - Coordinated public release of advisory
