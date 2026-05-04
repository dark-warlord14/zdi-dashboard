# ZDI-07-023: Apple QTJava toQTPointer() Pointer Arithmetic Memory Overwrite Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-023
- **ZDI-CAN:** ZDI-CAN-190
- **Date:** 2007-05-01
- **CVE:** CVE-2007-2175
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Dino A. Dai Zovi
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-023/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on systems with vulnerable installations of Apple's QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The flaw exists within the QuickTime Java extensions (QTJava.dll), specifically the routine toQTPointer() exposed through quicktime.util.QTHandleRef. A lack of sanity checking on the parameters passed to this routine, through the Java Virtual Machine (JVM), allows an attacker to write arbitrary values to memory. This can be leveraged to execute arbitrary code under the context of the current user. Example code execution vectors include Microsoft Internet Explorer, Mozilla Firefox and Apple Safari. This vulnerability affects the latest versions of both the MacOS and Windows operating systems, including MacOS 10.4.9 and Windows Vista.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://docs.info.apple.com/article.html?artnum=305446

## Disclosure Timeline

- 2007-04-23 - Vulnerability reported to vendor
- 2007-05-01 - Coordinated public release of advisory
