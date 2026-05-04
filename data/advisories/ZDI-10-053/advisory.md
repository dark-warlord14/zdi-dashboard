# ZDI-10-053: Sun Java Runtime Environment MIDI File metaEvent Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-053
- **ZDI-CAN:** ZDI-CAN-631
- **Date:** 2010-04-05
- **CVE:** CVE-2010-0844
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Sun Microsystems
- **Affected Products:** Java Runtime
- **Credit:** Peter Vreugdenhil (http://vreugdenhilresearch.nl)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-053/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Sun's Java Runtime Environment. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists within the handling of MIDI streams. When the code responsible for creating a MixerSequencer object from a MIDI stream encounters an 0xFF byte, it assumes it has reached a metaEvent. It then proceeds to parse out a variable-length field. By abusing the way this structure is stored an attacker can corrupt a pointer address later allowing a NULL byte write to an arbitrary memory address. This can be leveraged to execute remote code under the context of the user running the applet.

## Additional Details

Sun Microsystems has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technology/deploy/security/critical-patch-updates/javacpumar2010.html

## Disclosure Timeline

- 2009-12-10 - Vulnerability reported to vendor
- 2010-04-05 - Coordinated public release of advisory
