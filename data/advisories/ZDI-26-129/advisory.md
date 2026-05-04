# ZDI-26-129: Socomec DIRIS A-40 HTTP API Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-129
- **ZDI-CAN:** ZDI-CAN-23993
- **Date:** 2026-02-25
- **CVE:** CVE-2026-2491
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Socomec
- **Affected Products:** DIRIS A-40
- **Credit:** Dmitry "InfoSecDJ" Janushkevich of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-129/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of Socomec DIRIS A-40 power monitoring devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the web API implementation, which listens on TCP port 80 by default. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Socomec has issued an update to correct this vulnerability. More details can be found at: https://emea.socomec.com/en/resource-center/resource-type/cyber-vulnerabilities-601

## Disclosure Timeline

- 2025-03-11 - Vulnerability reported to vendor
- 2026-02-25 - Coordinated public release of advisory
- 2026-02-25 - Advisory Updated
