# ZDI-23-1174: (Pwn2Own) HP Color LaserJet Pro M479fdw msws Server-Side Request Forgery Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1174
- **ZDI-CAN:** ZDI-CAN-19683
- **Date:** 2023-08-24
- **CVE:** CVE-2023-35175
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** HP
- **Affected Products:** Color LaserJet Pro M479fdw
- **Credit:** nxhoang99, HaToan, QuangHV99 from VcsLab of Viettel Cyber Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1174/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of HP Color LaserJet Pro M479fdw printer. Authentication is not required to exploit this vulnerability. The specific flaw exists within the msws service. The issue results from the lack of proper validation of a URI prior to accessing resources. An attacker can leverage this vulnerability to execute code in the context of udwserv service.

## Additional Details

HP has issued an update to correct this vulnerability. More details can be found at: https://support.hp.com/us-en/document/ish_8651322-8651446-16/hpsbpi03851

## Disclosure Timeline

- 2022-12-28 - Vulnerability reported to vendor
- 2023-08-24 - Coordinated public release of advisory
