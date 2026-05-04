# ZDI-20-1207: Mitsubishi Electric MELSEC iQ-F Predictable TCP Sequence Number Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1207
- **ZDI-CAN:** ZDI-CAN-10966
- **Date:** 2020-09-08
- **CVE:** CVE-2020-16226
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Mitsubishi Electric
- **Affected Products:** MELSEC iQ-F
- **Credit:** Ta-Lun Yen of TXOne IoT/ICS Security Research Labs (Trend Micro)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1207/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Mitsubishi Electric MELSEC iQ-F. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of ACK packets. When generating ACK packets, the application uses a predictable sequence number. An attacker can leverage this vulnerability to execute arbitrary code in the context of the current process.

## Additional Details

Mitsubishi Electric has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-20-245-01

## Disclosure Timeline

- 2020-04-21 - Vulnerability reported to vendor
- 2020-09-08 - Coordinated public release of advisory
- 2020-09-17 - Advisory Updated
