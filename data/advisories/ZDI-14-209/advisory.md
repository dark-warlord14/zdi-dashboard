# ZDI-14-209: Hewlett-Packard IT Executive Scorecard CAP File Upload Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-209
- **ZDI-CAN:** ZDI-CAN-2117
- **Date:** 2014-06-18
- **CVE:** CVE-2014-2610
- **CVSS:** 7.1
- **CVSS Vector:** AV:N/AC:H/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** IT Executive Scorecard
- **Credit:** Mike Arnold (Bruk0ut)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-209/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard IT Executive Scorecard. Authentication is required to exploit this vulnerability. The specific flaw exists within the Content Acceleration Pack web application code. A file upload directory traversal vulnerability can be leveraged to execute code under the context of the SYSTEM user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c04341295

## Disclosure Timeline

- 2014-01-31 - Vulnerability reported to vendor
- 2014-06-18 - Coordinated public release of advisory
