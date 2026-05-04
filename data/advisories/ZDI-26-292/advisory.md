# ZDI-26-292: QNAP TS-453E QVRPro excpostgres Exposed Dangerous Method Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-292
- **ZDI-CAN:** ZDI-CAN-28327
- **Date:** 2026-04-15
- **CVE:** CVE-2026-22898
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** QNAP
- **Affected Products:** TS-453E
- **Credit:** Daniel FREDERIC from Fuzzinglabs, Julien COHEN-SCALI from Fuzzinglabs, Patrick VENTUZELO from Fuzzinglabs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-292/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of QNAP TS-453E devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the QVRPro Plugin. The issue results from an exposed dangerous method. An attacker can leverage this vulnerability to execute code in the context of the postgres user.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en-ca/security-advisory/qsa-26-07

## Disclosure Timeline

- 2026-01-22 - Vulnerability reported to vendor
- 2026-04-15 - Coordinated public release of advisory
- 2026-04-15 - Advisory Updated
