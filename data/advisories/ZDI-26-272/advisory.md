# ZDI-26-272: ATEN Unizon RpcProvider Missing Authentication Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-272
- **ZDI-CAN:** ZDI-CAN-29041
- **Date:** 2026-04-15
- **CVE:** CVE-2026-5057
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** ATEN
- **Affected Products:** Unizon
- **Credit:** Bobby Gould (@bobbygould5) of TrendAI Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-272/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of ATEN Unizon. Authentication is not required to exploit this vulnerability. The specific flaw exists within the RpcProvider class. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

ATEN has issued an update to correct this vulnerability. More details can be found at: https://www.aten.com/global/en/supportcenter/info/security-advisory/26/

## Disclosure Timeline

- 2026-01-30 - Vulnerability reported to vendor
- 2026-04-15 - Coordinated public release of advisory
- 2026-04-15 - Advisory Updated
