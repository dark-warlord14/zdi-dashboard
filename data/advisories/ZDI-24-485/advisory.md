# ZDI-24-485: LAquis SCADA LGX Report TextFile OpenWithoutMemory Path Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-485
- **ZDI-CAN:** ZDI-CAN-22469
- **Date:** 2024-05-22
- **CVE:** CVE-2024-5040
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** LAquis
- **Affected Products:** SCADA
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-485/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of LAquis SCADA. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the TextFile.OpenWithoutMemory method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

LAquis has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-24-142-01

## Disclosure Timeline

- 2023-11-15 - Vulnerability reported to vendor
- 2024-05-22 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
