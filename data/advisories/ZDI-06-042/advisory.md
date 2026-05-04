# ZDI-06-042: Verity Ultraseek Request Proxying Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-042
- **ZDI-CAN:** ZDI-CAN-039
- **Date:** 2006-11-15
- **CVE:** CVE-2006-5819
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Verity
- **Affected Products:** Ultraseek
- **Credit:** sullo / CIRT.net
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-042/
## Vulnerability Details

This vulnerability allows remote attackers to proxy web attacks and scan internal hosts through vulnerable installations of Verity Ultraseek. Authentication is not required to exploit this vulnerability. The specific flaw exists within the highlight script used to highlight search terms on spidered pages. An attacker can directly access the highlight script at '/highlight/index.html' to pass parameters to and retrieve content from arbitrary URLs. The same script can also be abused to enumerate otherwise inaccessible internal addresses and open ports. Ultraseek also exposes various information disclosure vulnerabilities through the following scripts: /help/urlstatusgo.html /help/header.html /help/footer.html /spell.html /coreforma.html /daterange.html /hits.html /hitsnavbottom.html /indexform.html /indexforma.html /languages.html /nohits.html /onehit1.html /onehit2.html /query.html /queryform0.html /queryform0a.html /queryform1.html /queryform1a.html /queryform2.html /queryform2a.html /quicklinks.html /relatedtopics.html /signin.html /subtopics.html /thesaurus.html /topics.html /hitspagebar.html /highlight/highlight.html /highlight/highlight_one.html /highlight/topnav.html Authenticated Ultraseek users can further abuse another vulnerability to retrieve arbitrary file contents from the underyling server through the '/admin/logfile.txt' script.

## Additional Details

Verity has issued an update to correct this vulnerability. More details can be found at: http://www.ultraseek.com/support/docs/RELNOTES.txt

## Disclosure Timeline

- 2006-05-09 - Vulnerability reported to vendor
- 2006-11-15 - Coordinated public release of advisory
