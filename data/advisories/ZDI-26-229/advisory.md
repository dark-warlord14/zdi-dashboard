# ZDI-26-229: OpenClaw Client PKCE Verifier Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-229
- **ZDI-CAN:** ZDI-CAN-29381
- **Date:** 2026-03-30
- **CVE:** CVE-2026-3691
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:N/A:N
- **Affected Vendors:** OpenClaw
- **Affected Products:** OpenClaw
- **Credit:** Peter Girnus (@gothburz), Demeng Chen (@DemengChen233), Project AESIR with TrendAI Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-229/
## Vulnerability Details

This vulnerability allows remote attackers to disclose stored credentials on affected installations of OpenClaw. User interaction is required to exploit this vulnerability in that the target must initiate an OAuth authorization flow. The specific flaw exists within the implementation of OAuth authorization. The issue results from the exposure of sensitive data in the authorization URL query string. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

OpenClaw has issued an update to correct this vulnerability. More details can be found at: https://github.com/openclaw/openclaw/security/advisories/GHSA-6g25-pc82-vfwp

## Disclosure Timeline

- 2026-02-25 - Vulnerability reported to vendor
- 2026-03-30 - Coordinated public release of advisory
- 2026-03-30 - Advisory Updated
