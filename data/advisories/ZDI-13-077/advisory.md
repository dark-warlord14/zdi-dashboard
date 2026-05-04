# ZDI-13-077: (Pwn2Own) Oracle Java FLV Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-077
- **ZDI-CAN:** ZDI-CAN-1827
- **Date:** 2013-05-10
- **CVE:** CVE-2013-0402
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** VUPEN Security [ http://www.vupen.com ]
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-077/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of FLV files. The issue lies in the parsing of a FLV file with two video tags using the On2 VP6 codec. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpuapr2013-1928497.html

## Disclosure Timeline

- 2013-04-26 - Vulnerability reported to vendor
- 2013-05-10 - Coordinated public release of advisory
