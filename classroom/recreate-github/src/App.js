import logo from './logo.svg';
import './App.css';
import NavigationBar from './components/NavigationBar';
import SearchBar from './components/SearchBar'
import LoginControls from './components/LoginControls';
import HeroSection from './components/HeroSection';
import NewsletterForm from './components/NewsletterForm';
import StatsBar from './components/StatsBar';

function App() {
  return (
    <main>
      <h1>Github</h1>
      <NavigationBar></NavigationBar>
      <SearchBar></SearchBar>
      <LoginControls></LoginControls>
      <HeroSection></HeroSection>
      <NewsletterForm></NewsletterForm>
      <StatsBar></StatsBar>
    </main>
  );
  
}

export default App;
