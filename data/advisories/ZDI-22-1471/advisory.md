# ZDI-22-1471: (0Day) Corel CorelDRAW Graphics Suite CGM File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1471
- **ZDI-CAN:** ZDI-CAN-16356
- **Date:** 2022-10-25
- **CVE:** CVE-2022-43613
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Corel
- **Affected Products:** CorelDRAW Graphics Suite
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1471/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Corel CorelDRAW Graphics Suite. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of CGM files. When parsing CGM files, the process does not properly validate the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Corel has issued an update to correct this vulnerability. More details can be found at: https://www.coreldraw.com/en/support/updates/cdgs2022/update.html

## Disclosure Timeline

- 2022-01-26 - Vulnerability reported to vendor
- 2022-10-25 - Coordinated public release of advisory
- 2023-05-24 - Advisory Updated
