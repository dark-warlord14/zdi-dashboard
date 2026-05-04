# ZDI-26-228: OpenClaw Canvas Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-228
- **ZDI-CAN:** ZDI-CAN-29311
- **Date:** 2026-03-30
- **CVE:** CVE-2026-3690
- **CVSS:** 7.4
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N
- **Affected Vendors:** OpenClaw
- **Affected Products:** OpenClaw
- **Credit:** Peter Girnus (@gothburz) and Project AESIR of TrendAI Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-228/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of OpenClaw. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the the authentication function for canvas endpoints. The issue results from improper implementation of authentication. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

OpenClaw has issued an update to correct this vulnerability. More details can be found at: https://github.com/openclaw/openclaw/security/advisories/GHSA-vvjh-f6p9-5vcf

## Disclosure Timeline

- 2026-02-20 - Vulnerability reported to vendor
- 2026-03-30 - Coordinated public release of advisory
- 2026-03-30 - Advisory Updated
