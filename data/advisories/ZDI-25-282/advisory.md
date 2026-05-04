# ZDI-25-282: Webmin CRLF Injection Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-282
- **ZDI-CAN:** ZDI-CAN-26502
- **Date:** 2025-05-01
- **CVE:** CVE-2025-2774
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Webmin
- **Affected Products:** Webmin
- **Credit:** hir0ot and tri.lm
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-282/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Webmin. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of CGI requests. The issue results from the lack of proper neutralization of CRLF sequences. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

fixed in Webmin 2.302

## Disclosure Timeline

- 2025-02-28 - Vulnerability reported to vendor
- 2025-05-01 - Coordinated public release of advisory
- 2025-05-01 - Advisory Updated
