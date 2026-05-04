# ZDI-26-227: OpenClaw Canvas Path Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-227
- **ZDI-CAN:** ZDI-CAN-29312
- **Date:** 2026-03-30
- **CVE:** CVE-2026-3689
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** OpenClaw
- **Affected Products:** OpenClaw
- **Credit:** Peter Girnus (@gothburz) and Project AESIR of TrendAI Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-227/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of OpenClaw. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of the path parameters provided to the canvas gateway endpoint. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of the service account.

## Additional Details

OpenClaw has issued an update to correct this vulnerability. More details can be found at: https://github.com/openclaw/openclaw/security/advisories/GHSA-jq4x-98m3-ggq6

## Disclosure Timeline

- 2026-02-20 - Vulnerability reported to vendor
- 2026-03-30 - Coordinated public release of advisory
- 2026-03-30 - Advisory Updated
