# ZDI-23-1798: PaperCut NG Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1798
- **ZDI-CAN:** ZDI-CAN-21500
- **Date:** 2023-12-15
- **CVE:** CVE-2023-6006
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** PaperCut
- **Affected Products:** NG
- **Credit:** Amol Dosanjh of Trend Micro and Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1798/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of PaperCut NG. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the pc-pdl-to-image process. The process loads an executable from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

PaperCut has issued an update to correct this vulnerability. More details can be found at: https://www.papercut.com/kb/Main/security-bulletin-november-2023/

## Disclosure Timeline

- 2023-07-04 - Vulnerability reported to vendor
- 2023-12-15 - Coordinated public release of advisory
