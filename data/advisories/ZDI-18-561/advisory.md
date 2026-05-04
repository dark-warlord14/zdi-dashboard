# ZDI-18-561: (Pwn2Own) Samsung Notes ZIP File Directory Traversal File Write Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-561
- **ZDI-CAN:** ZDI-CAN-5358
- **Date:** 2018-06-07
- **CVE:** CVE-2018-10501
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Samsung
- **Affected Products:** Notes
- **Credit:** MWR Labs - Alex Plaskett James Loureiro Robert Miller and Georgi Geshev
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-561/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Samsung Notes. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of ZIP files. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the application.

## Additional Details

Patched with Samsung Notes v. 2.0.02.31

## Disclosure Timeline

- 2017-11-05 - Vulnerability reported to vendor
- 2018-06-07 - Coordinated public release of advisory
- 2018-06-07 - Advisory Updated
