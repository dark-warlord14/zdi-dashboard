# ZDI-25-151: Progress Software Kemp LoadMaster mangle Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-151
- **ZDI-CAN:** ZDI-CAN-25708
- **Date:** 2025-03-18
- **CVE:** CVE-2025-1758
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Progress Software
- **Affected Products:** Kemp LoadMaster
- **Credit:** Nicholas Zubrisky (@NZubrisky) of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-151/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Progress Software Kemp LoadMaster. Authentication is not required to exploit this vulnerability. The specific flaw exists within the mangle executable. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the bal user.

## Additional Details

Progress Software has issued an update to correct this vulnerability. More details can be found at: https://docs.progress.com/bundle/release-notes_loadmaster-7-2-61-1/page/Security-Updates.html

## Disclosure Timeline

- 2024-11-13 - Vulnerability reported to vendor
- 2025-03-18 - Coordinated public release of advisory
- 2025-03-18 - Advisory Updated
