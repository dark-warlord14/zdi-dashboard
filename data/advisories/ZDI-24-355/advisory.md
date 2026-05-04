# ZDI-24-355: Wireshark NetScreen File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-355
- **ZDI-CAN:** ZDI-CAN-22164
- **Date:** 2024-03-28
- **CVE:** CVE-2023-6175
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Wireshark
- **Affected Products:** Wireshark
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-355/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Wireshark. User interaction is required to exploit this vulnerability in that the target must open a specially crafted packet capture file. The specific flaw exists within the parsing of packet capture files in the NetScreen format. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Wireshark has issued an update to correct this vulnerability. More details can be found at: https://www.wireshark.org/security/wnpa-sec-2023-29.html

## Disclosure Timeline

- 2023-10-17 - Vulnerability reported to vendor
- 2024-03-28 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
