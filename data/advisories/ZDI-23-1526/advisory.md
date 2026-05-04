# ZDI-23-1526: (0Day) MuseScore CAP File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1526
- **ZDI-CAN:** ZDI-CAN-20769
- **Date:** 2023-10-04
- **CVE:** CVE-2023-44428
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** MuseScore
- **Affected Products:** MuseScore
- **Credit:** Osori (Young Min Kim)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1526/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of MuseScore. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of CAP files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

05/08/23 – ZDI requested a PSIRT contact. 05/10/23 – ZDI received an automated support response. 07/26/23 – ZDI requested a PSIRT contact. 07/26/23 – ZDI received an automated support response. 09/26/23 – ZDI requested a PSIRT contact. 09/26/23 – ZDI received an automated support response. 10/03/23 – ZDI made multiple attempts to contact the vendor without success, and we’re publishing this case as a zero-day advisory in accordance with our disclosure policy. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-10-04 - Vulnerability reported to vendor
- 2023-10-04 - Coordinated public release of advisory
