# ZDI-15-624: Wireshark PCAPNG if_filter Arbitrary Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-624
- **ZDI-CAN:** ZDI-CAN-3139
- **Date:** 2015-12-08
- **CVE:** CVE-2015-7830
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Wireshark
- **Affected Products:** Wireshark
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-624/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Wireshark. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of PCAPNG files. The issue lies in the handling of the if_filter section within next-generation PCAP files. An attacker can leverage this vulnerability to execute arbitrary code under the context of the the current process.

## Additional Details

Wireshark has issued an update to correct this vulnerability. More details can be found at: https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11455

## Disclosure Timeline

- 2015-09-08 - Vulnerability reported to vendor
- 2015-12-08 - Coordinated public release of advisory
