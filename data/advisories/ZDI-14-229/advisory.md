# ZDI-14-229: Hewlett-Packard Universal CMDB mam-collectors Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-229
- **ZDI-CAN:** ZDI-CAN-2083
- **Date:** 2014-07-09
- **CVE:** CVE-2014-2615
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Universal CMDB
- **Credit:** Mike Arnold (Bruk0ut)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-229/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard Universal CMDB. Authentication is not required to exploit this vulnerability. The specific flaw exists within the mam-collectors servlet. The issue lies in the ability to download arbitrary files. A remote attacker can abuse this to disclose the credentials store that could result in remote code under the context of the process.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c04357076

## Disclosure Timeline

- 2014-03-07 - Vulnerability reported to vendor
- 2014-07-09 - Coordinated public release of advisory
