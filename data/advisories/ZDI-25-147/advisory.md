# ZDI-25-147: (0Day) NI Vision Builder AI VBAI File Processing Missing Warning Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-147
- **ZDI-CAN:** ZDI-CAN-22833
- **Date:** 2025-03-17
- **CVE:** CVE-2025-2450
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** NI
- **Affected Products:** Vision Builder AI
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-147/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of NI Vision Builder AI. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of VBAI files. The issue results from allowing the execution of dangerous script without user warning. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

04/26/24 – ZDI reported the vulnerability to the vendor 08/22/24 - ZDI asked for updates 09/27/24 - ZDI asked for updates 12/11/24 - ZDI asked for updates 12/19/24 – the vendor communicated that the reported behaviour was not a security issue 02/19/25 - ZDI notified the vendor of the intention to publish the case as a 0-day advisory

## Disclosure Timeline

- 2024-04-26 - Vulnerability reported to vendor
- 2025-03-17 - Coordinated public release of advisory
- 2025-03-17 - Advisory Updated
