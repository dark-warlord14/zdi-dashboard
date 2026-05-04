# ZDI-24-1314: PaperCut NG pc-web-print Link Following Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1314
- **ZDI-CAN:** ZDI-CAN-24042
- **Date:** 2024-10-02
- **CVE:** CVE-2024-8405
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** PaperCut
- **Affected Products:** NG
- **Credit:** Amol Dosanjh of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1314/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of PaperCut NG. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the pc-web-print service. By creating a junction, an attacker can abuse the service to create a file. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

PaperCut has issued an update to correct this vulnerability. More details can be found at: https://www.papercut.com/kb/Main/Security-Bulletin-May-2024

## Disclosure Timeline

- 2024-05-01 - Vulnerability reported to vendor
- 2024-10-02 - Coordinated public release of advisory
- 2024-10-02 - Advisory Updated
