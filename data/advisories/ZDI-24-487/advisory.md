# ZDI-24-487: LAquis SCADA LGX Report STRING READFROMFILE Path Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-487
- **ZDI-CAN:** ZDI-CAN-22468
- **Date:** 2024-05-22
- **CVE:** CVE-2024-5040
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N
- **Affected Vendors:** LAquis
- **Affected Products:** SCADA
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-487/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of LAquis SCADA. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the STRING.READFROMFILE method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of the current process.

## Additional Details

LAquis has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-24-142-01

## Disclosure Timeline

- 2023-11-15 - Vulnerability reported to vendor
- 2024-05-22 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
