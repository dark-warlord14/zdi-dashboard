# ZDI-10-060: Sun Java Runtime Environment MixerSequencer Invalid Array Index Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-060
- **ZDI-CAN:** ZDI-CAN-630
- **Date:** 2010-04-05
- **CVE:** CVE-2010-0842
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Sun Microsystems
- **Affected Products:** Java Runtime
- **Credit:** Peter Vreugdenhil ( http://vreugdenhilresearch.nl )
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-060/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Sun's Java Runtime Environment. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists within the handling of MixerSequencer objects. When this object is used to play a MIDI file, the GM_Song structure is populated with song data. In particular, it stores a integer value from the file and uses it later as an index into an array of function pointers. If this value is over 128 the process can be made to call a pointer outside the array. This can be leveraged to execute arbitrary code under the context of the user running the applet.

## Additional Details

Sun Microsystems has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technology/deploy/security/critical-patch-updates/javacpumar2010.html

## Disclosure Timeline

- 2009-12-10 - Vulnerability reported to vendor
- 2010-04-05 - Coordinated public release of advisory
