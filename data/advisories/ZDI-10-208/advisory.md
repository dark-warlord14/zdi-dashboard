# ZDI-10-208: Oracle Java Runtime HeadspaceSoundbank.nGetName BANK Record Size Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-208
- **ZDI-CAN:** ZDI-CAN-715
- **Date:** 2010-10-12
- **CVE:** CVE-2010-3559
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-208/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Oracle Java Runtime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the support for processing SoundBank files. While parsing BANK records, the HeadspaceSoundbank.nGetName function improperly sign-extends the one byte value into 4 bytes. It is later used as the size to a memcpy when operating on the BANK record's data. An attacker can abuse this to execute arbitrary code under the context of the user running the web browser.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpuoct2010-176258.html

## Disclosure Timeline

- 2010-06-23 - Vulnerability reported to vendor
- 2010-10-12 - Coordinated public release of advisory
