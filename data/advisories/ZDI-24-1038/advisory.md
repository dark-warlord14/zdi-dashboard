# ZDI-24-1038: PaperCut NG pc-web-print Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1038
- **ZDI-CAN:** ZDI-CAN-20972
- **Date:** 2024-07-31
- **CVE:** CVE-2024-3037
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** PaperCut
- **Affected Products:** NG
- **Credit:** Nicholas Zubrisky (@NZubrisky) and Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1038/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of PaperCut NG Server. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the pc-web-print service. By creating a symbolic link, an attacker can abuse the service to delete a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

PaperCut has issued an update to correct this vulnerability. More details can be found at: https://www.papercut.com/kb/Main/Security-Bulletin-May-2024

## Disclosure Timeline

- 2024-03-15 - Vulnerability reported to vendor
- 2024-07-31 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
